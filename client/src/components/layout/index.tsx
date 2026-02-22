import { Outlet } from 'react-router-dom';
import Navbar from '../navbar';
import Footer from '../footer';

const Layout = () => (
    <>
        <Navbar />
        <main className="min-h-[calc(100vh-8rem)]">
            <Outlet />
        </main>
        <Footer />
    </>
);

export default Layout;
