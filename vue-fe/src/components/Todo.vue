<template>
  <div class="font-mono pb-20">
    <div class="flex flex-col">
      <input type="text" placeholder="Put your tasks here" v-model="title" id="title" required name="title" class="w-3/5 border-4 mx-auto px-4 py-2 mb-2 text-center" />
      <input type="text" placeholder="Put your task details here" v-model="description" id="description" required name="description" class="w-3/5 border-4 mx-auto px-4 py-2 mb-2 text-center" />
      <button @click="addTodo()" class="shadow-xl bg-blue-500 hover:bg-blue-900 mx-auto px-4 py-1 rounded-md mb-2 text-white">ADD TO TODO</button>
    </div>
    <div class="flex md:flex-row flex-col">
      <div class="md:w-1/2 w-full mx-auto items-center p-2 md:border-r-2">
        <div class="w-full text-center">
          <h class="mx-auto font-bold text-2xl">TODO</h>
        </div>
        <!-- Pending Section -->
        <div v-for="task in unFinishedTasks" :key="task.id">
          <div class="relative flex flex-row w-full max-w-sm mx-auto overflow-hidden bg-gray-50 rounded-lg shadow-xl dark:bg-gray-800 my-4">
            <!-- Button for marking tasks Done -->
            <button @click="changeStatus(task)" class="flex items-center justify-center w-12 bg-red-500 hover:bg-gray-600 focus:outline-none hover:bg-opacity-25 border-2 rounded-l-xl">
              <div class="p-1 transition-colors duration-200 transform rounded-md text-gray-50 hover:text-gray-900">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
            </button>
            <!-- Button for editing tasks -->
            <button @click="editTask(task)" class="flex items-center justify-center w-14 bg-blue-400 hover:bg-gray-600 focus:outline-none hover:bg-opacity-25 border-2">
              <div class="p-1 transition-colors duration-200 transform rounded-md text-gray-50 hover:text-gray-900">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              </div>
            </button>
            <!-- Task Details -->
            <div class="px-4 py-2 -mx-3">
              <div class="mx-3">
                <span class="font-semibold text-red-500 dark:text-red-400">{{ task.title }}</span>
                <p class="text-sm text-gray-600 dark:text-gray-200">{{ task.description }}</p>
              </div>
            </div>
            <!-- Button for deleting tasks -->
            <button @click="deleteTask(task)" class="absolute right-0 bottom-0 top-0 flex items-center justify-center w-12 bg-red-500 hover:bg-gray-600 focus:outline-none hover:bg-opacity-25 rounded-r-xl">
              <div class="p-1 transition-colors duration-200 transform rounded-md text-gray-50 hover:text-gray-900">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </div>
            </button>
          </div>
        </div>
      </div>

      <!-- Done section  -->

      <div class="md:w-1/2 w-full mx-auto items-center p-2 md:border-l-2">
        <div class="w-full text-center">
          <h class="mx-auto font-bold text-2xl">DONE</h>
        </div>
        <div v-for="task in finishedTasks" :key="task.id">
          <!-- Revert Done status, Send back to pending -->
          <div class="relative flex w-full max-w-sm mx-auto overflow-hidden bg-gray-50 rounded-xl shadow-xl dark:bg-gray-800 my-4">
            <button @click="changeStatus(task)" class="flex items-center justify-center w-12 bg-green-500 hover:bg-gray-600 focus:outline-none hover:bg-opacity-25 border-2">
              <div class="p-1 transition-colors duration-200 transform rounded-md text-gray-50 hover:text-gray-900">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
                </svg>
              </div>
            </button>
            <!-- Edit Task details -->
            <button @click="editTask(task)" class="flex items-center justify-center w-14 bg-blue-400 hover:bg-gray-600 focus:outline-none hover:bg-opacity-25 border-2">
              <div class="p-1 transition-colors duration-200 transform rounded-md text-gray-50 hover:text-gray-900">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              </div>
            </button>
            <!-- Task Details -->
            <div class="px-4 py-2 -mx-3">
              <div class="mx-3">
                <span class="font-semibold text-green-500 dark:text-green-400">{{ task.title }}</span>
                <p class="text-sm text-gray-600 dark:text-gray-200">{{ task.description }}</p>
              </div>
            </div>
            <!-- Delete from section -->
            <button @click="deleteTask(task)" class="absolute right-0 bottom-0 top-0 flex items-center justify-center w-12 bg-green-500 hover:bg-gray-600 focus:outline-none hover:bg-opacity-25">
              <div class="p-1 transition-colors duration-200 transform rounded-md text-gray-50 hover:text-gray-900">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import TodoApi from "../axios/Todo-api";

    export default {
      name: 'Todo',
      data() {
        return {
          APIdata: [],
          title: "",
          description: ""

        }
      },
            methods: {
              changeStatus(task) {
                  task.complete = !task.complete

                  TodoApi.update(task.id, {
                    title: task.title,
                    description: task.description,
                    complete: task.complete,
                    })
              },

              retrieveTasks(){
                TodoApi.getAll()
                .then(response => {
                  this.APIdata = response.data;
                  console.log(response.data)
                })
                .catch(e=> {
                  console.log(e)
                })
              },

              addTodo() {
                var data = {
                    title: this.title,
                    description: this.description};
                    this.APIdata.push(data)

                TodoApi.create(data)
                 .then(response => {
                    console.log(response.data);
                    this.retrieveTasks();
                    this.resetFields();
                    })
                  .catch(e => {console.log(e);
                  this.retrieveTasks();
                    })
                },

                deleteTask(task){
                  TodoApi.delete(task.id)
                  .then(()=>
                  this.retrieveTasks()
                  )},

                editTask(task){
                  TodoApi.getDetails(task.id)
                  .then(response => {
                    this.title = response.data.title
                    this.description = response.data.description
                    this.deleteTask(task)
                  })
                  .catch(e => {console.log(e);})
                },

                resetFields() {
                  this.title = "",
                  this.description = ""
                }

          },
          computed: {
              finishedTasks(){
                  return this.APIdata.filter((task) => task.complete)
              },
              unFinishedTasks(){
                  return this.APIdata.filter((task) => !task.complete)
              }
          },
          mounted() {
            this.retrieveTasks();
          },
    }
</script>
