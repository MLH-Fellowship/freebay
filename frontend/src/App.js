import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import home from './pages/home';
import newItem from './pages/newItem';
import results from './pages/results';
import getItem from './pages/getItem';
function App() {
  return (
    <Router>
    <div>
       <Switch>
          <Route exact path="/" component={home}/>    
          <Route exact path="/newitem" component={newItem}/>  
          <Route exact path="/results" component={results}/>  
          <Route exact path="/getItem" component={getItem}/> 
           
          </Switch>
    </div>
</Router>
  );
}

export default App;
