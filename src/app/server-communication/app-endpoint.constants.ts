export interface RegisterRequest {
    username: string;
    email: string;
    password: string;
}

export interface RegisterResponse {
    idToken: string;
    expiresIn: string;
    refreshToken: string;
    localId: string;
}

export interface LoginRequest {
    username: string;
    password: string;
}

export interface LoginResponse {
    idToken: string;
    expiresIn: string;
    refreshToken: string;
    localId: string;
}

export interface SecuritysRequest {
    ticker: string;
}
