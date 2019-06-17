<template>
  <div>
    <p>Metrics:</p>
    <li>Population: {{ population }}</li>
    <li>Mumy Money: {{ mummy_money }}</li>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Init',
  data () {
    return {
      mummy_money: null,
      population: null
    }
  },
  methods: {
    getEndFromBackend () {
      const path = `http://localhost:5000/api/terminate`
      axios
        .get(path)
        .then(response => {
          this.mummy_money = response.data.mummy_money
          this.population = response.data.population
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getEndFromBackend()
  }
}
</script>
