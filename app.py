from flask import Flask, render_template, jsonify
from backend import Inversors
from backend import Members
from backend import Metrics
from tinydb import TinyDB, Query
from flask_cors import CORS
import random

def cleanDB():
    db = TinyDB('members.json')
    db.purge_tables()
    db = TinyDB('inversors.json')
    db.purge_tables()
    db = TinyDB('metrics.json')
    db.purge_tables()

def generate_population():
    population = random.randint(50, 100)
    print("Generating population...")
    for i in range(population):
        i = Inversors.Inversors().insert()
    print('Generating metrics...')
    # Save pupulation into the Metrics
    Metrics.Metrics().generate()
    Metrics.Metrics().add_population(population)

def init_members():
    for i in range(10):
        inversor = Inversors.Inversors().select()
        Members.Members().insert(inversor.id, 0)
        Metrics.Metrics().add_mummy_money()

def simulate_week():
    members_active = Members.Members().count()
    count_new_members = 0
    count_leave_members = 0
    for m in Members.Members().getMembersActive():
        i = Inversors.Inversors()
        i.get(m['inversor_id'])
        p_new_member = random.random()
        if i.probability_find_member(members_active) < p_new_member:
                p_accept_member = random.random()
                if i.probability_candidate_accept() < p_accept_member:
                        inversor = Inversors.Inversors().select()
                        if inversor.id != 0:
                                Members.Members().insert(inversor.id, i.id)
                                Metrics.Metrics().add_mummy_money()
                                gain = i.money + 100
                                Metrics.Metrics().subtract_mummy_money()
                                i.save_money(gain)
                                count_new_members = count_new_members + 1

        if i.max_weeks() < i.weeks:
                if i.money < 500:
                        member = Members.Members()
                        member.get(m.doc_id)
                        member.remove()
                        count_leave_members = count_leave_members + 1
        
        i.add_week()

    total_members = Members.Members().count()
    inversors = []
    for m in Members.Members().getMembersActive():
            i = Inversors.Inversors()
            i.get(m['inversor_id'])
            inversor = {
                'id': i.id,
                'money': i.money
            }
            inversors.append(inversor)

    metrics = Metrics.Metrics()
    metrics.get()

    response = {
        'new_members': count_new_members,
        'members_left': count_leave_members,
        'total_members': total_members,
        'members': inversors,
        'mummy_money': metrics.mummy_money

    }
    return jsonify(response)

def getMembers():
    metrics = Metrics.Metrics()
    metrics.get()
    inversors = []
    for m in Members.Members().getMembersActive():
            i = Inversors.Inversors()
            i.get(m['inversor_id'])
            inversor = {
                'id': i.id,
                'money': i.money
            }
            inversors.append(inversor)
 
    response = {
        'new_members': 0,
        'members_left': 0,
        'total_members': Members.Members().count(),
        'members': inversors,
        'mummy_money': metrics.mummy_money
    }
    return jsonify(response)


#APP
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/init')
def init_app():
    cleanDB()
    generate_population()
    init_members()
    response = {
        'status': 'OK'
    }
    return jsonify(response)

@app.route('/api/simulate')
def simlate():
    return simulate_week()

@app.route('/api/members')
def members():
    return getMembers()

@app.route('/api/terminate')
def get_metrics():
    metrics= Metrics.Metrics()
    metrics.get()
    response = {
        'population': metrics.population,
        'mummy_money': metrics.mummy_money
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

