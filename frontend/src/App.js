import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import Home from './pages/Home';
import NewItem from './pages/NewItem';
import Results from './pages/Results';
import GetItem from './pages/GetItem';

function App() {
  return (
    <Router>
    <div>
       <Switch>
          <Route exact path="/" component={Home}/>    
          <Route exact path="/newitem" component={NewItem}/>  
          <Route exact path="/results" component={Results}/>  
          <Route exact path="/getItem" component={GetItem}/> 
           
          </Switch>
    </div>
</Router>
  );
}

export default App;
