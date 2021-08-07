<template>
<div>
   <div class="animate-bounce mt-10"> <img class=" mx-auto transform rotate-180 h-20" alt="Vue logo" src="./assets/logo.png"></div>
  <Todo/>
</div>
</template>

<script>
import Todo from './components/Todo.vue';

export default {
  name: 'App',
  components: {
    Todo
  }
}
</script>

