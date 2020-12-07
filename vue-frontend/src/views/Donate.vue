<template>
    <div>
        <h1>What would you like to donate?</h1>
        <div class="form-group">
            <label>Name:</label>
            <input type="text" id="inputTitle" v-model="item.title" placeholder="">
            <label>Category:</label>
            <select v-model="item.category">
                <option v-for="category in categories" :key="category">
                    {{category}}
                </option>
            </select>
            <label>Description:</label>
            <textarea v-model="item.description" placeholder="Max 500 words.."></textarea>
            <label>Insert Image:</label>
            <input type="file" @change="onFileSelected">
            <label>Location:</label>
            <select v-model="item.location">
                <option v-for="country in countries" :key="country">
                    {{country}}
                </option>
            </select>
        </div>
        <button class="donate-button" @click="donateItem()">
            Donate
        </button>
    </div>
</template>

<script>

export default {
  name: 'Donate',
  data() {
      return{
          item: {
            id: 0,
            title: '',
            category:'',
            description: '',
            image: '',
            location: ''
          },
          categories: [
            'Food',
            'Clothes',
            'Books',
            'Hobbies',
            'Sport',
            'Furniture',
            'Other'
            ],
          countries: [
              'United States',
              'United Kingdom',
              'Mexico',
              'Canada',
              'Italy',
              'Nigeria',
              'Brazil',
              'Armenia',
              'Egypt'
          ],
          selectedFile: null
      }
  },
  components: {
  },
  methods: {
      onFileSelected(event) {
          this.selectedFile = event.target.files[0];
      },
      donateItem() {
          console.log(this.item);
      }
  }
}
</script>

<style scoped>
* {
 margin: 0;
 padding: 5px;
 box-sizing: border-box;
 font-family: 'montserrat', sans-serif;
 }

.form-group {
 font-family: 'montserrat', sans-serif;
 text-align: left;
 margin: 50px;
 padding-left: 100px;
 display: grid;
 grid-template-columns: 150px 300px;
}

.donate-button {
 appearance: none;
 outline: none;
 border: none;
 background: none;
 cursor: pointer;
 
 display: inline-block;
 padding: 15px 25px;
 background-image: linear-gradient(to right, #CC2E5D, #FF5858);
 border-radius: 8px;
 
 color: #FFF;
 font-size: 18px;
 font-weight: 700;
 
 box-shadow: 3px 3px rgba(0, 0, 0, 0.4);
 transition: 0.4s ease-out;
}
</style>