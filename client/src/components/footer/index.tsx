const Footer = () => {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="bg-gray-900 text-white py-8 mt-1">
            <div className="max-w-6xl mx-auto px-4">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
                    <div>
                        <h3 className="font-bold mb-4">About</h3>
                        <p className="text-gray-400">Adless Kitchen - Your cooking companion</p>
                    </div>
                    <div className="relative group">
                        <h3 className="font-bold mb-4">Links</h3>
                        <ul className="space-y-2 text-gray-400 md:absolute md:bg-gray-800 md:p-4 md:rounded md:shadow-lg md:invisible md:group-hover:visible md:group-hover:opacity-100 md:opacity-0 transition-opacity">
                            <li><a href="#" className="hover:text-white block">Home</a></li>
                            <li><a href="#" className="hover:text-white block">Recipes</a></li>
                            <li><a href="#" className="hover:text-white block">Contact</a></li>
                        </ul>
                    </div>
                    <div className="relative group">
                        <h3 className="font-bold mb-4">Follow</h3>
                        <ul className="space-y-2 text-gray-400 md:absolute md:bg-gray-800 md:p-4 md:rounded md:shadow-lg md:invisible md:group-hover:visible md:group-hover:opacity-100 md:opacity-0 transition-opacity">
                            <li><a href="https://github.com/lsanchez17" className="hover:text-white block">GitHub</a></li>
                            <li><a href="https://www.linkedin.com/in/codebyluis" className="hover:text-white block">LinkedIn</a></li>
                        </ul>
                    </div>
                </div>
                <div className="border-t border-gray-700 pt-8 text-center text-gray-400">
                    <p>&copy; {currentYear} Adless Kitchen. All rights reserved.</p>
                </div>
            </div>
        </footer>
    );
};

export default Footer;