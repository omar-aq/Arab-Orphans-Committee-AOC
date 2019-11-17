import React, {Component} from 'react';
import {Route, Switch} from 'react-router-dom';

// import pages here 
import About from './pages/about/About';
import Homepage from './pages/home/Homepage' 
import Gallery from './pages/gallery/Gallery'
import Faq from './pages/faq/Faq'
import Students from './pages/our_students/Students'
import Register from './pages/register/Register'
import Login from './pages/login/Login';
import StudentsPage from './pages/students_pages/Students'
import Blog from './pages/blog/Blog'
import Dashboard from './pages/dashboard_users/Dashboard'
class App extends Component {
  render() {
    return (
      <main> 
        {/* <Switch> */}
          <Route exact path="/homepage" component={Homepage} />
          <Route exact path="/about" component={About} />
          <Route exact path="/gallery" component={Gallery} />
          <Route exact path="/students" component={Students} />
          <Route exact path="/faq" component={Faq} />
          <Route exact path="/register" component={Register} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/studentspage" component={StudentsPage} />
          <Route exact path="/blog" component={Blog} />
          <Route exact path="/dashborad" component={Dashboard} />
          {/* </Switch> */}
      </main>
    )
  }
} 



export default App;
