import React from 'react'
import { Link } from 'react-router-dom'
import { CgProfile } from "react-icons/cg";


function Header() {
  return (
    <section className='bg-red-500 w-full h-28'>
        <div className='bg-blue-300 flex justify-between p-4'>
            <div className='p-5'>
                <Link to={"/"}>College Dekho</Link>
            </div>

            <div className="text-white">
                <ul className='flex'>
                    <Link 
                    to={"/login"}
                    className='px-5 bg-zinc-600 m-2 py-1 rounded-full'
                    >Login</Link>

                    <Link 
                    to={"/signup"}
                    className='px-5 bg-zinc-600 m-2 py-1 rounded-full'
                    >Signup</Link>

                    <Link 
                    to={"/colleges"}
                    className='px-5 bg-zinc-600 m-2 py-1 rounded-full'
                    >Colleges</Link>


                    <Link 
                    to={"/profile"}
                    className='px-5  m-2 py-1 rounded-full'
                    > <CgProfile className='text-3xl' />
                    </Link>
                </ul>
            </div>
        </div>
    </section>
  )
}

export default Header