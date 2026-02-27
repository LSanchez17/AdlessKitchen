import Layout from '@/components/layout'
import App from "@/App"
import Login from "@/modules/login"
import Signup from "@/modules/signup"
import { createBrowserRouter } from 'react-router-dom'
import Home from '@/modules/home'

const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            { index: true, element: <App /> },
            { path: 'login', element: <Login /> },
            { path: 'signup', element: <Signup /> },
            { path: 'home', element: <Home /> },
        ],
    },
])

export default router