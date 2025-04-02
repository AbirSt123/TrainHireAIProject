# Angular Frontend

## Overview
This is an Angular 17.3.0 frontend application for an interview simulation platform. It provides a user interface for authentication, interview recording, and resume management.

## Features
- User authentication
- Video recording and playback
- Resume management interface
- Lottie animations
- Responsive design with Bootstrap and Tailwind CSS

## Setup Instructions
1. Extract the zipped project to your desired location
2. Navigate to the Frontend directory:
   ```bash
   cd path/to/extracted/Frontend
   ```
3. Install dependencies:
   ```bash
   npm install
   ```

## Development Server
Run the development server:
```bash
npm start
```
The application will be available at `http://localhost:4200/`

## Building the Project
To build the project for production:
```bash
npm run build
```

## Directory Structure
```
frontend/
├── src/
│   ├── app/              # Angular components and services
│   ├── assets/           # Static assets
│   ├── environments/     # Environment configurations
│   ├── styles.css        # Global styles
└── angular.json          # Angular configuration
```

## Dependencies
- Angular 17.3.0
- Bootstrap 5.3.3
- Tailwind CSS 3.4.16
- Video.js 8.21.0
- RecordRTC 5.6.2
- ngx-cookie-service 19.1.0

## License
[MIT License](LICENSE)
