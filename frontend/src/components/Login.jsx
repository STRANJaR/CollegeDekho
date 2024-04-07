import React from 'react'
import { Link } from 'react-router-dom'


function Login() {
  return (
    <section className='bg-fuchsia-50 text-light-100 h-screen w-full'>
      <div className=' h-screen'>
          <div className='flex flex-col ml-96 mr-96 relative top-28 '>

            <Link
            to={'/college-login'}
            className='bg-fuchsia-700  text-white hover:bg-fuchsia-800 shadow-md transition-all  text-center p-4 rounded-sm my-3'
            >

            Login as College
            </Link>

            <Link
            to={'/faculty-login'}
            className='bg-fuchsia-700  text-white hover:bg-fuchsia-800 shadow-md transition-all  text-center p-4 rounded-sm my-3'
            >
            Login as Faculty
            </Link>
            
            <Link
            to={'/student-login'}
            className='bg-fuchsia-700  text-white hover:bg-fuchsia-800 shadow-md transition-all  text-center p-4 rounded-sm my-3'
            >
            Login as Student
            </Link>

            
          </div>
        
      </div>
    </section>
  )
}

export default Login