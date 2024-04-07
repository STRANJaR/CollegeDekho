import axios from 'axios';
import React, { useState } from 'react'
import { Link } from 'react-router-dom';

function CollegeLogin() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = (e) => {
        e.preventDefault();

        try {
            const userData = {
                username,
                password
            }
            axios.post(`http://127.0.0.1:8000/college_login/`, userData)
            .then((response)=> console.log(response))
        } catch (error) {
            console.log(error);
        }
    }
  return (
    <section className="h-screen w-full ">

    <div className="bg-fuchsia-50 h-screen flex justify-around">

      {/* Left side image  */}
      <div className="w-full bg-fuchsia-700 text-center">
        
        <h1 className="relative top-64 font-semibold text-light-100 text-3xl">College Login</h1>

      </div>

      {/* Right side signup  */}
      <div className="h-auto w-full p-4 ml-12">

        <h1 className="text-3xl py-5 p">Login</h1>

        <form onSubmit={handleLogin}>
          <div className="flex flex-col"> 


          <label 
            className="text-xs py-2"
            htmlFor="username">
              Username: 
              </label>

              <input 
              className="p-3 outline-none border-2 border-fuchsia-400 w-96"
              placeholder="Enter Your Username..."
              type="text" 
              name="username" 
              defaultValue={username} 
              onChange={(e)=> setUsername(e.target.value)} 
              required={true}/>

            

            <label
            className="text-xs py-2"
            htmlFor="password"
            >
              Password: 
              </label>

              <input 
              className="p-3 outline-none  border-2 border-fuchsia-400 w-96"
              placeholder="Enter Your Password..."
              type="password" 
              name="password" 
              defaultValue={password} 
              onChange={(e)=> setPassword(e.target.value)} 
              required={true} />
        
            <button 
            className="bg-fuchsia-500 text-light-100 rounded-sm p-3 w-96 mt-4"
            type="submit"
            >Login
            </button>

            <p className="pt-5">Already registerd?
            <Link
            to="/login"
            className="font-medium hover:underline"
            >
            Sign in to your account
            </Link> 
            </p>
          </div>

        </form>

      </div>
    </div>
  </section>
  )
}

export default CollegeLogin