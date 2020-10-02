import React from 'react';
import {
  BrowserRouter as Router,
  Route
} from "react-router-dom";
// import './App.css';
import About from './challenge/About';
import Sixty from './challenge/sixty';
import Thirty from './challenge/thirty';
import Header from './components/Header';
import Navbar from './Navbar';

function App() {
  return (
    <Router >

      <Navbar />
      <Header />
      <Route exact path='/' component={Thirty} />
      <Route exact path='/sixty' component={Sixty} />
      <Route exact path='/about' component={About} />
    </Router>
  );
}

export default App;
