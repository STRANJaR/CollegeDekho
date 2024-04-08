import React from 'react'
import { Link } from 'react-router-dom'
import { FaUniversity } from "react-icons/fa";


function Signup() {

    
  return (
    <section className=' h-screen w-full'>
      <div className='bg-dark-100 h-screen'>
          <div className='flex flex-col ml-96 mr-96 relative top-28 '>

            <Link
            to={'/college-register'}
            className='bg-fuchsia-700  text-light-100 hover:bg-fuchsia-800 shadow-md transition-all  text-center p-4 rounded-sm my-3'
            >
              {/* <FaUniversity /> */}

            Register as College
            </Link>

            <Link
            to={'/faculty-register'}
            className='bg-fuchsia-700  text-light-100 hover:bg-fuchsia-800 shadow-md transition-all  text-center p-4 rounded-sm my-3'
            >
            Register as Faculty
            </Link>
            
            <Link
            to={'/student-register'}
            className='bg-fuchsia-700  text-light-100 hover:bg-fuchsia-800 shadow-md transition-all  text-center p-4 rounded-sm my-3'
            >
            Register as Student
            </Link>

            
          </div>
        
      </div>
    </section>
  )
}

export default Signup