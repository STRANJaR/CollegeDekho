import React from 'react'
import { Link } from 'react-router-dom'


function Signup() {

    
  return (
    <section className="h-screen w-full bg-bodyPrimary">
      
      <div className="bg-bodyPrimary h-screen flex justify-around  mx-20">

        {/* Left side image  */}
        <div className="w-full bg-blueShade text-center">
          {/* <img src={""} width="400"  alt="" /> */}
          <h1 className="relative top-64 font-semibold text-whiteText text-3xl">TODO APP</h1>

        </div>

        {/* Right side signup  */}
        <div className="h-auto w-full p-4 ml-12">

          <h1 className="text-3xl py-5 p">Register</h1>

          <form onSubmit={""}>
            <div className="flex flex-col"> 

              {/* <label 
              className="text-xs py-2"
              htmlFor="fullName"
              >
                Full Name: 
              </label>

                <input 
                className="p-3 outline-none border w-96"
                placeholder="Enter Your Full Name..."
                type="text" 
                name="fullName" 
                defaultValue={""} 
                onChange={""} 
                required={true} /> */}

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
                defaultValue={""} 
                onChange={""} 
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
                defaultValue={""} 
                onChange={""} 
                required={true} />

              
              

              <lable 
              className="text-xs py-2"
              htmlFor="password"
              >
                Password: 
                </lable>

                <input 
                className="p-3 outline-none  border w-96"
                placeholder="Enter Your Password..."
                type="password" 
                name="password" 
                defaultValue={""} 
                onChange={""} 
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

export default Signup