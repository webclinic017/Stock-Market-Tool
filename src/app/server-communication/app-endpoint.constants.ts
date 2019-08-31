export interface RegisterRequest {
    username: string;
    email: string;
    password: string;
}

export interface RegisterResponse {
    message: string;
    result: {
        email: string,
        password: string,
        username: string,
        __v: number,
        _id: string
    };
}

export interface LoginRequest {
    username: string;
    password: string;
}

export interface LoginResponse {
    token: string;
}

export interface SecuritysRequest {
    ticker: string;
}
