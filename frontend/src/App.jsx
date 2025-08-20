import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import React from 'react'
import LoginPage from './pages/LoginPage'
import AdminDashboard from './Dashoards/AdminDashboard'
import DoctorDashboard from './Dashoards/DoctorDashboard'
import ReceptionistDashboard from './Dashoards/ReceptionistDashboard'
import PharmasistDashboard from './Dashoards/PharmasistDashboard'
const App = () => {
  return (
    <Router>

      <Routes>
        <Route path='/' element={<LoginPage/>}/>
        <Route path='/doctorDashboard' element={<DoctorDashboard/>} />
        <Route path='/adminDashboard' element={<AdminDashboard/>} />
        <Route path='/pharmacistDashboard' element={<PharmasistDashboard/>} />
        <Route path='/receptionistDashboard' element={<ReceptionistDashboard/>} />
      </Routes>
    </Router>
  )
}

export default App