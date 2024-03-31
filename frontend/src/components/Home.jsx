import React, { useEffect, useState } from 'react'
import axios from "axios"

function Home() {
  const [data, setData] = useState({})

  useEffect(()=> {
    axios.get('http://127.0.0.1:8000/get_faculty_data/1')
    .then((response)=> {
      console.log(response.data)
      setData(response.data)
    })
  }, [])
  return (
    <div className='h-screen w-full content-center text-center'>
      <h1>{data.id}</h1>
      <h1>{data.name}</h1>
      <h1>{data.skills}</h1>
      <h1>{data.experience}</h1>
      <h1>{data.experience}</h1>
    </div>
  )
}

export default Home