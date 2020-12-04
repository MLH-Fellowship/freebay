import React, { useState, useEffect } from 'react';
const { NavLink, Redirect, useHistory } = require("react-router-dom");

function Home() {
    const [keyword, setKeyword] = useState('')
    const [category, setCategory] = useState('')
    const [country, setCountry] = useState('')
    const history = useHistory();

    const handleSubmit = (event) => {
        if (event)
          event.preventDefault();
        console.log(keyword)
        console.log(category)
        console.log(country)
        history.push('/results');
      }   
   
 
    return (
      <div>
          <p>home</p>
          <NavLink to='/NewItem'>I want to donate</NavLink>
          <form onSubmit={handleSubmit}>
            <label>What are you looking for?
                <input 
                    type="text"
                    value={keyword}
                    onChange={e => {
                        setKeyword(e.target.value);
                    }}
                    />
            </label>
            <br></br>
            <label>Category
                <select value={category} 
                onChange={e => {setCategory(e.target.value);}}>
                    <option value="clothes">Clothes</option>
                    <option value="food">Food</option>
                    <option value="furniture">Furniture</option>
                    <option value="other">Other</option>
                </select>
            </label>
            <br></br>
            <label>Where?
                <select value={country} 
                onChange={e => {setCountry(e.target.value);}}>
                    <option value="Italy">Italy</option>
                    <option value="US">US</option>
                </select>
            </label>
            <br></br>
            <input type='submit'/>
      </form>
      </div>
      
    );
  }
  export default Home;