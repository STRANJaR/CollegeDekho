import React from 'react'
import { Link } from 'react-router-dom'
import { CgProfile } from "react-icons/cg";


function Header() {
  return (
    <section className='bg-dark-100 w-full h-auto'>
        <div className='bg-dark-100  text-light-100 flex justify-between mx-14'>
            <div className=''>
                <Link to={"/"}>Logo</Link>
            </div>

            <div className="text-white">
                <ul className='flex'>
                    <Link 
                    to={"/login"}
                    className='px-5 m-2 py-1 rounded-sm hover:bg-fuchsia-600 transition-all shadow-md'
                    >Sign in</Link>

                    <Link 
                    to={"/signup"}
                    className='px-5 bg-fuchsia-800 m-2 py-1 rounded-sm hover:bg-fuchsia-600 transition-all shadow-md'
                    >Signup</Link>

                    {/* <Link 
                    to={"/colleges"}
                    className='px-5 bg-zinc-600 m-2 py-1 rounded-full'
                    >Colleges</Link> */}


                    {/* <Link 
                    to={"/profile"}
                    className='px-5  m-2 py-1 rounded-full'
                    > <CgProfile className='text-3xl' />
                    </Link> */}
                </ul>
            </div>
        </div>
    </section>
  )
}

export default Header