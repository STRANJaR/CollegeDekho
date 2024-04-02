import React from 'react'
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';

function StudentSignup() {

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
        axios.post(`http://127.0.0.1:8000/college_signup/`, userData)
        .then((response)=>{
        console.log(response);
        })
    } catch (error) {
        console.log("Something went wrong while register college", error);
    }
    }


  return (
    <section className="h-screen w-full bg-bodyPrimary">

    <div className="bg-bodyPrimary h-screen flex justify-around  mx-20">

      {/* Left side image  */}
        <div className="w-full bg-teal-600 text-center">
        {/* <img src={""} width="400"  alt="" /> */}
        <h1 className="relative top-64 font-semibold text-whiteText text-3xl">Student Register</h1>

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
                className="p-3 outline-none border w-96"
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
                className="p-3 outline-none border w-96"
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
                className="p-3 outline-none  border w-96"
                placeholder="Enter Your Password..."
                type="password" 
                name="password" 
                defaultValue={password} 
                onChange={(e)=> setPassword(e.target.value)} 
                required={true} />
        
            <button 
            className="bg-primaryColor text-whiteText rounded-sm p-3 w-96 mt-4"
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

export default StudentSignup