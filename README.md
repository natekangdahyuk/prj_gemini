# prj_gemini

이 문서는 `prj_gemini` 프로젝트의 기술 스택, 아키텍처, 개발 규칙 및 워크플로에 대한 포괄적인 컨텍스트를 제공합니다.

## 1. 프로젝트 개요

### 1.1 목적
이 프로젝트는 Gemini 모델의 강력한 기능을 터미널 환경으로 가져오는 것을 목표로 하는 AI 에이전트 또는 관련 도구로 보입니다. Python 백엔드와 TypeScript/React 기반의 CLI 프론트엔드를 결합한 하이브리드 구조를 가집니다.

### 1.2 아키텍처 및 기술 스택
- **하이브리드 구조**: 핵심 로직 및 모델 상호작용은 Python으로, 사용자 인터페이스(CLI)는 TypeScript/Node.js로 구현됩니다.
- **Python 백엔드**:
    - Gemini 모델과의 직접적인 상호작용(`GeminiModel` 클래스), 병렬 API 호출, 재시도 로직 등을 처리합니다.
    - `BaseLlm`을 상속하는 고수준 `Gemini` 클래스를 통해 비동기 작업, 스키마 변환 등을 지원합니다.
    - 배포 스크립트 생성 및 종속성 확인과 같은 인프라 관련 작업을 수행합니다.
- **TypeScript/Node.js 프론트엔드 (CLI)**:
    - **UI**: [React](https://reactjs.org/)와 [Ink](https://github.com/vadimdemedes/ink)를 사용하여 대화형 CLI 사용자 인터페이스를 구축합니다.
    - **런타임**: Node.js (`v18.x` 또는 그 이상)를 기반으로 실행됩니다.
    - **패키지 관리**: `npm`을 사용하여 의존성을 관리합니다.

### 1.3 예제 코드
- `sum.py`: 두 숫자의 합을 계산하는 간단한 Python 스크립트입니다. 프로젝트의 Python 스크립트 실행 환경을 테스트하는 데 사용할 수 있습니다.

## 2. 빌드 및 실행

### 2.1 주요 명령어
- **품질 검사 (Preflight)**: 모든 변경 사항은 제출 전에 아래의 'preflight' 명령어를 통해 종합적인 검증을 거쳐야 합니다. 이 명령어는 빌드, 테스트, 타입 체크, 린트를 모두 포함합니다.
  ```bash
  npm run preflight
  ```
- **개별 스크립트**: `package.json`의 `scripts` 섹션에 정의된 `build`, `test`, `typecheck`, `lint` 등을 개별적으로 실행할 수도 있습니다.

### 2.2 의존성 관리
- **Node.js**: `package.json` 파일에 명시된 의존성은 `npm install`을 통해 설치합니다.
- **Python**: `requirements.txt` 파일에 명시된 의존성은 `pip install -r requirements.txt`를 통해 설치해야 합니다. (파일 존재 시)

## 3. 개발 규칙

### 3.1 JavaScript/TypeScript 스타일 가이드
- **Plain Objects 선호**: React 및 전반적인 코드 유지보수와의 상호 운용성을 위해, `class` 구문보다는 TypeScript `interface` 또는 `type`으로 정의된 **순수 JavaScript 객체(Plain JavaScript Objects)** 사용을 최우선으로 합니다.

### 3.2 테스트 규칙
- **테스트 프레임워크**: **Vitest**를 기본 테스트 프레임워크로 사용합니다. (`describe`, `it`, `expect`, `vi`)
- **파일 위치**: 테스트 파일(`*.test.ts` 또는 `*.test.tsx`)은 테스트 대상 소스 파일과 **같은 위치(co-location)**에 둡니다.
- **Mocking**:
    - `vi.mock()`을 사용하여 ES 모듈을 모킹합니다.
    - `fs`, `os`와 같이 모듈 레벨 상수에 영향을 주는 중요한 의존성의 모킹 코드는 테스트 파일의 **최상단**에 위치해야 합니다.
    - `ink-testing-library`를 사용하여 React (Ink) 컴포넌트를 테스트합니다. `lastFrame()`으로 출력을 검증합니다.
- **Git 브랜치**: 주 개발 브랜치는 `main` 입니다.
