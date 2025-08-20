import React, { use, useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
const [username,setUsername]=useState("")
const[password,setPassword]=useState("")
const [error,setError]=useState("")
const navigate=useNavigate()
const loginButton=async(e)=>{
    e.preventDefault();
    try{
        const res=await axios.post("http://localhost:8000/api/users/login/",{username,password})
        localStorage.setItem("access",res.data.access)
        localStorage.setItem("refresh",res.data.refresh)
        localStorage.setItem("user",JSON.stringify(res.data.user))
        if (res.data.user.role==="doctor"){
            navigate("/doctordashboard")
        }
        else if(res.data.user.role==="admin"){
            navigate("/admindashboard")
        }
        else if(res.data.user.role==="pharmacist"){
            navigate("/pharmacistdashboard")
        }
        else if(res.data.user.role==="receptionist"){
            navigate("/receptionistdashboard")
        }else{
            console.log("no dashboard")
        }
    }catch(err){
        setError("invalid username password")
    }
    
}
  return (
    <div className="login_container">
        <div className="form">
            <h1>Login to redirect to the dashboards</h1>
            <form >
                <input type="text" value={username} onChange={(e)=>setUsername(e.target.value)} />
                <input type="password" value={password} onChange={(e)=>setPassword(e.target.value)}  />
                <button onClick={loginButton}>Login</button>
            </form>
        </div>

    </div>
  )
}

export default LoginPage