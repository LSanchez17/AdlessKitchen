const Home = () => {
    return (
        <div className="min-h-screen bg-gray-50 p-8">
            <div className="max-w-6xl mx-auto">
                <h1 className="text-3xl font-bold text-gray-900 mb-8">Dashboard</h1>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div className="bg-white rounded-lg shadow p-6">
                        <div className="h-40 bg-gray-100 rounded flex items-center justify-center text-gray-500">
                            Card 1
                        </div>
                    </div>

                    <div className="bg-white rounded-lg shadow p-6">
                        <div className="h-40 bg-gray-100 rounded flex items-center justify-center text-gray-500">
                            Card 2
                        </div>
                    </div>

                    <div className="bg-white rounded-lg shadow p-6">
                        <div className="h-40 bg-gray-100 rounded flex items-center justify-center text-gray-500">
                            Card 3
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Home;