let vm = new Vue({
    el: '#app-4',
    data: {
      todos: [
        { text: 'Learn JavaScript' },
        { text: 'Learn Vue' },
        { text: 'Build something awesome' }
      ],
      inputField: "",
    },
    methods: {
        addTodo: function() {
            this.todos.push({text: this.inputField})
        },
        removeTodos: function(todo) {
            // console.log(todo)
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
    }
})