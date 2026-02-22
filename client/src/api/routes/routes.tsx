import { createBrowserRouter } from "react-router"
import Layout from '@/components/layout'
import App from "@/App"
import Login from "@/modules/login"
import Signup from "@/modules/signup"

const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            { index: true, element: <App /> },
            { path: 'login', element: <Login /> },
            { path: 'signup', element: <Signup /> },
        ],
    },
])

export default router