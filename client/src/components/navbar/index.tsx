import { useLogoutMutation } from "@/api/endpoints/user/user_api";
import { logout, selectIsUserLoggedIn } from "@/modules/user/user_slice";
import { useAppDispatch, useAppSelector } from "@/store/hooks";
import { Link } from "react-router-dom";

const Navbar = () => {
    const dispatch = useAppDispatch();
    const isUserLoggedIn = useAppSelector(state => selectIsUserLoggedIn(state));
    const [logoutMutation] = useLogoutMutation();

    const handleSignOut = async () => {
        await logoutMutation();
        dispatch(logout());
    };

    return (
        <nav className="flex justify-between items-center px-4 py-2 mb-1 border-b border-gray-700 bg-gray-900 text-white">
            <div className="font-bold text-lg">
                <Link to="/" className="no-underline text-white">
                    AdlessKitchen
                </Link>
            </div>

            <div className="flex items-center gap-2">
                {isUserLoggedIn ? (
                    <>
                        <Link to="/recipes" className="px-3 py-1 rounded border border-gray-700 bg-gray-800 text-white no-underline hover:bg-gray-700">
                            Recipes
                        </Link>
                        <Link to="/generate" className="px-3 py-1 rounded border border-gray-700 bg-gray-800 text-white no-underline hover:bg-gray-700">
                            Generate
                        </Link>
                        <button onClick={handleSignOut} className="px-3 py-1 rounded border border-gray-700 bg-gray-800 text-white hover:bg-gray-700">
                            Sign out
                        </button>
                    </>
                ) : (
                    <>
                        <Link to="/signup" className="px-3 py-1 rounded border border-gray-700 bg-gray-800 text-white no-underline hover:bg-gray-700">
                            Sign up
                        </Link>
                        <Link to="/login" className="px-3 py-1 rounded border border-gray-700 bg-gray-800 text-white no-underline hover:bg-gray-700">
                            Log in
                        </Link>
                    </>
                )}
            </div>
        </nav>
    );
};

export default Navbar;