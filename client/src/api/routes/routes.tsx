import Layout from '@/components/layout'
import App from "@/App"
import Login from "@/modules/login"
import Signup from "@/modules/signup"
import { createBrowserRouter, Navigate, useLocation } from 'react-router-dom'
import Home from '@/modules/home'

function RequireAuth({ children }: { children: React.ReactNode }) {
    const location = useLocation();
    const token = localStorage.getItem('token');

    if (!token) {
        return <Navigate to="/login" state={{ from: location }} replace />;
    }
    return children;
}

const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            { index: true, element: <App /> },
            { path: 'login', element: <Login /> },
            { path: 'signup', element: <Signup /> },
            { path: 'home', element: <RequireAuth><Home /></RequireAuth> },
        ],
    },
])

export default router