interface LoginRequest {
    email: string;
    password: string;
}

interface AuthenticatedResponse {
    accessToken: string;
    user: {
        id: number;
        email: string;
        firstName: string;
        lastName: string;
    };
}

interface SignupRequest {
    email: string;
    password: string;
}

export type { LoginRequest, AuthenticatedResponse, SignupRequest }