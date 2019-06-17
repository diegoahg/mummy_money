<template>
  <div>
    <p>Wait the OK while the population is generate</p>
    <p>{{ status }}</p>
    <div v-html="buttonHTML"></div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Init',
  data () {
    return {
      status: '',
      buttonHTML: null
    }
  },
  methods: {
    getInitFromBackend () {
      const path = `http://localhost:5000/api/init`
      axios
        .get(path)
        .then(response => {
          this.status = response.data.status
          this.buttonHTML = `<a href="/simulate">Start Mummy Money Program!</a>`
        })
        .catch(error => {
          console.log(error)
        })
    },
    getStatus () {
      this.status = this.getInitFromBackend()
    }
  },
  created () {
    this.getStatus()
  }
}
</script>
