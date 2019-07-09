import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

export interface RegisterResponse {
    idToken: string;
    expiresIn: string;
    refreshToken: string;
    localId: string;
}

export interface LoginResponse {
    idToken: string;
    expiresIn: string;
    refreshToken: string;
    localId: string;
}

@Injectable({ providedIn: 'root' })
export class AppEndpointService {

    constructor(private http: HttpClient) { }

    // Register a new user.
    public register(email: string, password: string, username: string): Observable<RegisterResponse> {
        return this.http.post<RegisterResponse>(
            '/register',
            {
                username,
                email,
                password
            }
        )
        .pipe(
            catchError(errorRes => {
                let errorMessage = 'An unknown error occurred!';
                if (!errorRes.error || !errorRes.error.error) {
                    return throwError(errorMessage);
                }
                switch (errorRes.error.error.message) {
                    case 'EMAIL_EXISTS':
                        errorMessage = 'An account with this email already exists.';
                }
                return throwError(errorMessage);
            })
        );
    }

    // Login an existing user.
    public login(email: string, password: string, username: string): Observable<RegisterResponse> {
        return this.http.post<LoginResponse>(
            '/login',
            {
                password,
                username
            }
        );
    }

}
