<template>
   <div class="container">
      <button type="button" class="btn btn-primary">{{ msg }}</button>
   </div>
</template>

<script>
  import axios from 'axios'

  export default{
    name: 'ping',
      data() {
           return {
	       msg: 'Heelo, This is Ping.vue component'
	   }
      },
    methods:{
      getMessage (){
        const path = 'http://localhost:5000/api/ping'
        axios.get(path)
          .then((res) => {
	    this.msg = res.data;
	  })
      }
   },
   created (){
     this.getMessage()
   }
  } 
</script>
