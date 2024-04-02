import React from 'react'
import { Link } from 'react-router-dom'
import { FaUniversity } from "react-icons/fa";


function Signup() {

    
  return (
    <section className='bg-red-200 h-screen w-full'>
      <div className='bg-red-300 h-auto'>
        <div className=''>
          <div className='flex flex-col'>

            <Link
            to={'/college-register'}
            className='bg-green-200 w-96 text-center p-4 rounded-md my-3'
            >
              {/* <FaUniversity /> */}

            Register as College
            </Link>
            
            <Link
            className='bg-green-200 w-96 text-center p-4 rounded-md my-3'
            >
            Register as Faculty
            </Link>
            <Link
            className='bg-green-200 w-96 text-center p-4 rounded-md my-3'
            >
            Register as Student
            </Link>

            
          </div>
        </div>
      </div>
    </section>
  )
}

export default Signup