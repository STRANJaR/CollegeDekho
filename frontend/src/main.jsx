import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import Layout from './Layout.jsx'
import Home from './components/Home.jsx'
import Colleges from './components/Colleges.jsx'
import JoinCollege from './components/JoinCollege.jsx'
import Profile from './components/Profile.jsx'
import Signup from './components/Signup.jsx'
import FacultySignup from './components/Faculty/FacultySignup.jsx'
import CollegeSignup from './components/College/CollegeSignup.jsx'
import StudentSignup from './components/Student/StudentSignup.jsx'
import Login from './components/Login.jsx'
import CollegeLogin from './components/College/CollegeLogin.jsx'
import FacultyLogin from './components/Faculty/FacultyLogin.jsx'
import StudentLogin from './components/Student/StudentLogin.jsx'
import CreateCollegeProfile from './components/College/CreateCollegeProfile.jsx'


const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout/>,
    children: [
      {
        path: "/",
        element: <Home/>
      },
      {
        path: "/colleges",
        element: <Colleges/>
      },
      {
        path: "/profile",
        element: <Profile/>
      },
      {
        path: "/signup",
        element: <Signup/>
      },
      {
        path: "/faculty-register",
        element: <FacultySignup/>
      },
      {
        path: "/college-register",
        element: <CollegeSignup/>
      },
      {
        path: "/student-register",
        element: <StudentSignup/>
      },
      {
        path: "/login",
        element: <Login/>
      },
      {
        path: "/college-login",
        element: <CollegeLogin/>
      },
      {
        path: "/faculty-login",
        element: <FacultyLogin/>
      },
      {
        path: "/student-login",
        element: <StudentLogin/>
      },
      {
        path: "/create-college-profile",
        element: <CreateCollegeProfile/>
      },
    ]
  }
])
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
