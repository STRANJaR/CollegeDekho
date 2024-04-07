import axios from 'axios';
import React, { useState } from 'react'
import toast, { Toaster } from 'react-hot-toast';

function CreateCollegeProfile() {
    const [college_name, setCollege_name] = useState('');
    const [logo, setLogo] = useState('');
    const [images, setImages] = useState('');
    const [description, setDescription] = useState('');
    const [location, setLocation] = useState('');
    const [established_date, setEstablished_date] = useState('');
    const [website, setWebsite] = useState('');
    const [student_population, setStudent_population] = useState('');
    const [faculty_population, setFaculty_population] = useState('');
    const [affiliated_by, setAffiliated_by] = useState('');
    const [college_type, setCollege_type] = useState('');
    const [college_code, setCollege_code] = useState('');

    console.log(affiliated_by, college_code)

    const handleSubmit = (e) => {
        e.preventDefault();

        try {
            const collegeData = {
                college_name,
                logo,
                images,
                description,
                location,
                established_date,
                website,
                student_population,
                faculty_population,
                affiliated_by,
                college_code
            }
            axios.post(`http://127.0.0.1:8000/create_college_profile/`, collegeData)
            .then((response) => {
                console.log(response);
                toast.success(response.data.message)
            })
        } catch (error) {
            console.log(error);
            toast.error("Opps ! something went wrong")
        }
    }
  return (
    <>
    <Toaster/>
    <section className='bg-dark-100 text-light-100 h-screen'>
        <div className='h-screen '>
            <form
            className=''
            onSubmit={handleSubmit}>
                <div className='flex justify-evenly p-10'>
                    {/* Left Form  */}
                    <div className="flex flex-col">

                        <label 
                        className=' text-sm py-2'
                        htmlFor="college_name">
                            College Name :
                            </label>
                        <input
                        className='p-3 bg-dark-100 outline-none border-2 border-fuchsia-400 w-96' 
                        type="text" 
                        name="college_name" 
                        id="college_name" 
                        value={college_name}
                        onChange={((e) => setCollege_name(e.target.value))}
                        />

                        <label 
                        className=' text-sm py-2'
                        htmlFor="website">
                            Website : 
                            </label> 
                        <input 
                        className='p-3 bg-dark-100  outline-none border-2 border-fuchsia-400 w-96'
                        type="text" 
                        name="website" 
                        id="website" 
                        onChange={((e) => setWebsite(e.target.value))}
                        value={website}
                        />
                        
                        <label 
                        className=' text-sm py-2'
                        htmlFor="student_population">
                            Student Population : 
                            </label>
                        <input 
                        className='p-3  bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="text" 
                        name="student_population" 
                        id="student_population"
                        onChange={((e) => setStudent_population(e.target.value))}
                        value={student_population}
                        />

                        <label 
                        className=' text-sm py-2'
                        htmlFor="faculty_population">
                            Faculty Population : 
                            </label>
                        <input 
                        className='p-3 bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="text" 
                        name="faculty_population" 
                        id="faculty_population" 
                        onChange={((e) => setFaculty_population(e.target.value))}
                        value={faculty_population}
                        />

                        <label 
                        className=' text-sm py-2'
                        htmlFor="affiliated_by">
                            Affiliated By : 
                            </label>
                        <input 
                        className='p-3 bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="text" 
                        name="affiliated_by" 
                        id="affiliated_by" 
                        onChange={((e) => setAffiliated_by(e.target.value))}
                        value={affiliated_by}
                        />

                        <label 
                        className=' text-sm py-2'
                        htmlFor="college_type">
                            College Type : 
                            </label>
                        <input 
                        className='p-3 bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="text" 
                        name="college_type" 
                        id="college_type" 
                        onChange={((e) => setCollege_type(e.target.value))}
                        value={college_type}
                        />


                        

                    </div>
                    {/* Right Form  */}
                    <div className="flex flex-col">
                    <label 
                        className=' text-sm py-2'
                        htmlFor="college_code">
                            College Code : 
                            </label>
                        <input 
                        className='p-3 bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="text" 
                        name="college_code" 
                        id="college_code" 
                        value={college_code}
                        onChange={((e) => setCollege_code(e.target.value))}
                        />

                    <label 
                        className=' text-sm py-2'
                        htmlFor="location">
                            Location : 
                            </label>
                        <input 
                        className='p-3 bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="text" 
                        name="location" 
                        id="location" 
                        onChange={((e) => setLocation(e.target.value))}
                        value={location}
                        />

                    <label 
                        className=' text-sm py-2'
                        htmlFor="established_date">
                            Established Date : 
                            </label>
                        <input 
                        className='p-3  bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="date" 
                        name="established_date" 
                        id="established_date" 
                        onChange={((e) => setEstablished_date(e.target.value))}
                        value={established_date}
                        />

                    <label 
                        className=' text-sm py-2'
                        htmlFor="logo">
                            Logo : 
                            </label>
                        <input 
                        className='p-2 bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="file" 
                        name="logo" 
                        id="logo" 
                        onChange={((e) => setLogo(e.target.files.length[0]))}
                        value={logo}
                        />

                    <label 
                        className=' text-sm py-2'
                        htmlFor="images">
                            College Image : 
                            </label>
                        <input 
                        className='p-2 bg-dark-100 outline-none border-2 border-fuchsia-400 w-96'
                        type="file" 
                        name="images" 
                        id="images" 
                        onChange={((e) => setImages(e.target.files.length[0]))}
                        />
                        
                        <label 
                        className='text-sm py-2'
                        htmlFor="description">
                            Description : 
                        </label>
                        <textarea 
                        className='bg-dark-100 outline-none border-2 border-fuchsia-400 '
                        name="description" 
                        id="description" 
                        cols="10" 
                        rows="3"
                        value={description}
                        onChange={((e)=> setDescription(e.target.value))}
                        ></textarea>


                    </div>
                </div>
                <div className='flex justify-center'>
                    
                <button 
                className='px-40 py-5  bg-fuchsia-500 hover:bg-fuchsia-600 transition-all rounded-sm'
                type="submit">Create Profile </button>
                </div>
            </form>
        </div>

        <div className="h-40 bg-dark-100">

        </div>
    </section>
    </>

  )
}

export default CreateCollegeProfile