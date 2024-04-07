import React, { useEffect, useState } from 'react'
import axios from "axios"

function Home() {
  
  // useEffect(()=> {
  //   axios.get('http://127.0.0.1:8000/get_faculty_data/1')
  //   .then((response)=> {
  //     console.log(response.data)
  //     setData(response.data)
  //   })
  // }, [])

  return (
    <section className=' bg-dark-100 text-light-100 h-screen w-full '>
      <div className=' h-48'>
        {/* <div className=' h-auto w-auto rounded-full shadow-5xl shadow-fuchsia-500'> heo</div> */}
        <a 
        className='text-center'
        href="#">Link</a>
        <div className='relative top-48 flex flex-col text-center mx-20'>
          <h1 className='text-[80px] text-fuchsia-100 pb-8 font-black'>Accelerate Sales Growth with Expert Marketing Strategies</h1>

          <p className='text-1xl mx-56'>Experience the transformative power of our expert marketing strategies as we partner with you to elevate your brand's digital presence. Let us take your brand to new heights online!

</p>
        </div>
      </div>
    </section>
  )
}

export default Home