<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Home from './components/Home'
import Login from './components/Login'
import Register from './components/Register'

export default {
  name: 'App',
  components: {
    navbar: Navbar,
    home: Home,
    login: Login,
    register: Register,
  }
}
</script>

<style>

</style>
