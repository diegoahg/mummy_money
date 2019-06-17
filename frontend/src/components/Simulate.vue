<template>
  <div>
    <p>Simulatation week {{ weeks }} (next week in 10 seconds)</p>
    <p>Mummy has MM$: {{ mummy_money }}</p>
    <p>Members that left the program: {{ members_left }}</p>
    <p>Members added to the program: {{ new_members }}</p>
    <p>Total Members: {{ total_members }}</p>
    <table align="center">
        <th>
            <td>Member</td>
            <td>MM$</td>
        </th>
        <tr v-for="member in members" :key="member.id" >
            <td>{{member.id}}</td>
            <td>{{member.money}}</td>
        </tr>
    </table>
    <a href="/end">Do you wanna finish the program</a>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Init',
  data () {
    return {
      mummy_money: 0,
      new_members: 0,
      members_left: 0,
      total_members: 0,
      members: null,
      weeks: 1
    }
  },
  methods: {
    getSimulateFromBackend () {
      const path = `http://localhost:5000/api/simulate`
      axios
        .get(path)
        .then(response => {
          this.mummy_money = response.data.mummy_money
          this.new_members = response.data.new_members
          this.members_left = response.data.members_left
          this.total_members = response.data.total_members
          this.members = response.data.members
          this.weeks++
        })
        .catch(error => {
          console.log(error)
        })
    },
    getStartMembersFromBackend () {
      const path = `http://localhost:5000/api/members`
      axios
        .get(path)
        .then(response => {
          this.mummy_money = response.data.mummy_money
          this.new_members = response.data.new_members
          this.members_left = response.data.members_left
          this.total_members = response.data.total_members
          this.members = response.data.members
        })
        .catch(error => {
          console.log(error)
        })
    }
  },

  created () {
    this.getStartMembersFromBackend()

    setInterval(function () {
      this.getSimulateFromBackend()
    }.bind(this), 10000)
  }
}
</script>
