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
      }
    ]
  }
])
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
