<template>
  <div>
    <h1>Items</h1>
    <label>Name:</label>
    <input type="text" v-model="search" placeholder="Search Items..."/>
    <label>Category</label>
    <select v-model="searchCat">
        <option v-for="category in categories" :key="category">
            {{category}}
        </option>
    </select>
    <label>Location:</label>
      <select v-model="searchLoc">
          <option v-for="country in countries" :key="country">
              {{country}}
          </option>
      </select>
    <div class="item-display">
      <div v-for="Item in filteredItems" :key="Item.id">
        <div class="item-title">{{Item.title}}</div>
        <img :src="Item.image" width="128" height="128" /><br/>
        <button class="button" @click="selectItem(Item); showModal = true">
          More Information
        </button>
        <transition name="fade" appear>
          <div class="modal-overlay" v-if="showModal" @click="showModal = false"></div>
        </transition>
        <transition name="slide" appear>
          <div class="modal" v-if="showModal">
          <h1>{{myItem.title}}</h1>
          <img :src="myItem.image" width="128" height="128" /><br/>
          <h4>Location: {{myItem.location}}</h4>
          <p>Description: {{myItem.description}}</p>
          <button class="button" @click="showModal = false">
            Close
          </button>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>


<script>

export default {
  name: 'Items',
  components: {
  },
  data() {
    return {
      showModal:false,
      myItem: {},
      search: '',
      searchCat: '',
      searchLoc: '',
      categories: [
        '',
        'Food',
        'Clothes',
        'Books',
        'Hobbies',
        'Sport',
        'Furniture',
        'Other'
      ],
      countries: [
        '',
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
      Items: [
        {
          id: 1,
          category: "Clothes",
          title: "Shoes",
          description: "Adidas White Superstars",
          image: "https://assets.adidas.com/images/h_840,f_auto,q_auto:sensitive,fl_lossy/4e894c2b76dd4c8e9013aafc016047af_9366/Superstar_Shoes_White_FV3284_01_standard.jpg",
          location: "United States"
        },
        {
          id: 2,
          category: "Clothes",
          title: "Shirt",
          description: "Black T-Shirt",
          image: "https://i.imgur.com/VYLZsoD.jpg",
          location: "Mexico"
        },
        {
          id: 3,
          category: "Food",
          title: "Pizza",
          description: "Slice of Pepperoni Pizza",
          image: "https://upload.wikimedia.org/wikipedia/commons/e/ef/Fat_Slice_pepperoni_pizza_slice.JPG",
          location: "Italy"
        },
        {
          id: 4,
          category: "Sport",
          title: "Basketball",
          description: "WILSON Evolution Basketball",
          image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfBypU4kOIIdM6L6wTzg7pNty-CED5-fmx_g&usqp=CAU",
          location: "United Kingdom"
        }
      ]
    };
  },
  methods: {
    selectItem(Item) {
      this.myItem = Item;
    }
  },
  computed: {
    filteredItems: function() {
      return this.Items.filter((item) => {
        return item.title.match(this.search) && item.category.match(this.searchCat) && item.location.match(this.searchLoc);
      })
    }
  }
}
</script>

<style scoped>
  * {
 margin: 0;
 padding: 0;
 box-sizing: border-box;
}

body {
 font-family: 'montserrat', sans-serif;
}

.button {
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

.modal-overlay {
 position: absolute;
 top: 0;
 left: 0;
 right: 0;
 bottom: 0;
 z-index: 98;
 background-color: rgba(0, 0, 0, 0.3);
}

.modal {
 position: fixed;
 top: 50%;
 left: 50%;
 transform: translate(-50%, -50%);
 z-index: 99;
 
 width: 100%;
 max-width: 400px;
 background-color: #FFF;
 border-radius: 16px;
 
 padding: 25px;
}

.fade-enter-active,
.fade-leave-active {
 transition: opacity .5s;
}

.fade-enter,
.fade-leave-to {
 opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
 transition: transform .5s;
}

.slide-enter,
.slide-leave-to {
 transform: translateY(-50%) translateX(100vw);
}

.item-display {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

.item-title {
  font-family: 'montserrat', sans-serif;
  font-size: 60px;
  padding: 15px;
}
</style>

