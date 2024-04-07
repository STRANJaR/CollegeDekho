import React from 'react'
import { Link } from 'react-router-dom'
import { CgProfile } from "react-icons/cg";


function Header() {
  return (
    <section className='bg-light-100 border-b-2 border-fuchsia-600 w-full h-auto'>
        <div className='bg-dark-100 py-2 text-fuchsia-50 font-semibold flex justify-evenly '>
            <div className='flex'>
                <Link to={"/"}>Logo</Link>
            </div>


            <div className="">
                <ul className="flex  text-[14px]">
                    <Link 
                    to={'/create-college-profile'}
                    className='px-5 m-2 font-light py-1 rounded-sm hover:text-fuchsia-400 transition-all shadow-md'>
                        College Profile
                    </Link>
                    <Link 
                    to={"/colleges"}
                    className='px-5 m-2 py-1 font-light rounded-sm hover:text-fuchsia-400 transition-all shadow-md'>
                        Colleges
                    </Link>
                    <Link 
                    to={""}
                    className='px-5 m-2 py-1 rounded-sm font-light hover:text-fuchsia-400 transition-all shadow-md'>
                        Contact Us
                    </Link>
                </ul>
            </div>
            <div className="text-light font-light">
                <ul className='flex'>
                    <Link 
                    to={"/login"}
                    className='px-5 m-2 py-1 rounded-sm hover:text-fuchsia-400 transition-all shadow-md'
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