const prepareHeaders = (extraOptions: {}) => {
    const token = localStorage.getItem('token');

    if (token) {
        extraOptions = {
            ...extraOptions,
            headers: {
                ...(extraOptions as any)?.headers,
                Authorization: `Bearer ${token}`,
            },
        };
    }

    return extraOptions;
}

export default prepareHeaders;