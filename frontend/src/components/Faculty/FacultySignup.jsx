import axios from 'axios'
import React, { useEffect, useState } from 'react'
import toast, { Toaster } from 'react-hot-toast';
import { Link } from 'react-router-dom'


function FacultySignup() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  console.log(username, email, password)
  const handleSubmit = (e)=>{
    try {
      e.preventDefault();

      const userData = {
        username,
        email,
        password
      }
      axios.post(`http://127.0.0.1:8000/faculty_signup/`, userData)
      .then((response)=>{
        console.log(response);
        toast.success(response.data.message)
      })
      .catch((err)=> {
        toast.error(err.response.data.email[0])
        
      })
    } catch (error) {
      console.log("Something went wrong while signup faculty", error);
    }
  }
  return (
    <section className="h-screen w-full bg-bodyPrimary">
        <Toaster/>
    <div className="bg-fuchsia-50 h-screen flex justify-around">

      {/* Left side image  */}
      <div className="w-full bg-fuchsia-700 text-center">
        {/* <img src={""} width="400"  alt="" /> */}
        <h1 className="relative top-64 font-semibold text-light-100 text-3xl">Faculty Register</h1>

      </div>

      {/* Right side signup  */}
      <div className="h-auto w-full p-4 ml-12">

        <h1 className="text-3xl py-5 p">Register</h1>

        <form onSubmit={handleSubmit}>
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
            htmlFor="email"
            className="text-xs py-2"
            >
              Email: 
            </label>

              <input 
              className="p-3 outline-none border-2 border-fuchsia-400 w-96"
              placeholder="Enter Your Email..."
              type="email" 
              name="email" 
              defaultValue={email} 
              onChange={(e)=> setEmail(e.target.value)} 
              required={true} />

            

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
            className="bg-fuchsia-500 text-light-100 rounded-sm p-3 w-96 mt-4 hover:bg-fuchsia-600"
            type="submit"
            >Register
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

export default FacultySignup