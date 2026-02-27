interface LoginRequest {
    email: string;
    password: string;
}

interface SignupRequest {
    email: string;
    password: string;
}

export type { LoginRequest, SignupRequest }