import React, {useState, useEffect} from 'react'
import axios from 'axios'

function Colleges() {

    const [colleges, setColleges] = useState([]);

    useEffect(()=>{
        axios.get(`http://127.0.0.1:8000/get_college_list/`)
        .then((response)=> {
            setColleges(response.data.results)
            console.log(response);
        })
    }, [])
  return (
    <>
    <section className='h-screen w-full bg-white'>
        {colleges.map((college)=> (
            <div key={college.id}>
        <div className='bg-green-200 flex justify-between mx-10 p-7 mt-2 rounded-md '>
            <div>
                <img src={college.logo} width="100xl" alt="" />
            </div>

            <div className='px-7'>
                <h1 className='font-black'>{college.college_name}</h1>
                <p className='font-mono mt-2'>{college.description}</p>
            </div>
        </div>
    </div> 
        ))}
{/*         
        <div>
        <div className='bg-green-200 flex justify-between mx-10 p-7 mt-2 rounded-md '>
            <div>
                <img src={'https://upload.wikimedia.org/wikipedia/commons/2/24/LEGO_logo.svg'} width="100xl" alt="" />
            </div>

            <div className='px-7'>
                <h1 className='font-black'>KIHEAT</h1>
                <p className='font-mono mt-2'>{college.}</p>
            </div>
        </div>
    </div>  */}
    </section>
    </>
  )
}

export default Colleges