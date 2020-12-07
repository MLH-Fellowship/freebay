<template>
  <body>
  <div id="app">
    <Header>Freebay</Header>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/items">Items</router-link> |
      <router-link to="/donate">Donate</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
  </body>
</template>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 10px;
}

#nav a {
  font-weight: bold;
  color: #ffc300;
}

#nav a.router-link-exact-active {
  color: #C70039;
}
header {
  height: 60px;
  background-image: linear-gradient(to right,#C70039, #ffc300);
  box-shadow: 2px 2px 5px #ffc300;
  text-align: center;
  font-size: 30px;
  padding-top: 15px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  color: #fff;
}

body {
  background-image: linear-gradient(to bottom right,#C70039, #fff);
}
</style>
