# 한글 서술형 수리지능 Dataset

서술형 수리지능 문제 (Math Word Problem, MWP)는 수학적 관계가 언어와 숫자 표현으로 주어질 때, 이를 이용해 문제에서 요구하는 정보를 도출하는 문제 입니다.

기존의 관련 분야 연구들은 영어로 구축된 데이터셋에 집중되어 있어 한국어 문제에 사용하기 어렵다는 단점이 있습니다. 이러한 문제를 해결하기 위해 학습과 테스트에 활용할 다양한 유형의 한국어 서술형 수리지능 문제 데이터셋을 제공하는 것이 이 저장소의 목적입니다.

데이터셋은 서술형 수리지능 문제와 그에 해당하는 Python code형태의 답안이 포함되어 있습니다. Python code의 규칙은 [Python code 레이블](LABEL_RULE.md)에 상술되어 있습니다.

## Getting Started

본 데이터셋은 수리지능 문제의 source에 따라 아래와 같이 분류됩니다.

* [MAWPS](MAWPS/) : 기존 영문 데이터셋 (MAWPS/MATHQA)를 한글로 번역한 후 정제한 문제 
* [HANDCRAFT](HANDCRAFT/) 공개된 초등/중등 서술형 수학 문제를 가공하여 만든 문제

기존 영문 데이터셋은 단순 사칙연산만을 다루고 있으며, 공개된 초등/중등 서술형 수학 문제를 가공하여 만든 데이터셋에서 다양한 유형의 문제를 확인할 수 있습니다.

### 데이터셋 구성 (MAWPS)

MAWPS/MATHQA기반 데이터셋([MAWPS/](MAWPS/))은 problem과 answer마다 나누어져 json형식으로 저장되어있습니다.
먼저 Problem파일들의 구조는 다음과 같습니다.
```
{
	Problem-Number(str) : {
		"question": Problem-State(str)
	},
	...
}
```

각 문항별로 번호화 그에 해당하는 지문이 question에 들어있습니다.

Answer파일의 구조는 다음과 같습니다.
```
{
	Answer-Number(str) : {
		"answer": value(str, int),
		"equation": Python-Code,
		"QL": List[int]
	},
	...
}
```
문제 번호와 동일한 번호에 해당 정답에 관한 정보들이 있습니다.
"answer" key에는 그 문항의 결과 답안이 있으며, "equation" key에는 결과 답안을 생성하는 Python code가 있습니다. "QL"은 문제를 파싱하여 생성한 Quantity list입니다.

~~MAWPS데이터셋은 총 2000문항을 지원하는 것이 목표입니다. 현재 약 1200여개 이상의 문항이 지원되고 있습니다.~~
MAWPS데이터셋은 총 2000문항을 지원되고 있습니다.



### 데이터셋 구성 (HANDCRAFT)

~~초등/중등 수학 문제에서 직접 가공하여 만든 데이터셋([HANDCRAF/](HANDCRAFT/))은 현재 xlsx파일로 지원되고 있으나, 추후에 json파일로 통합하는 script를 제공하겠습니다.~~

초등/중등 수학 문제에서 직접 가공하여 만든 데이터셋([HANDCRAF/](HANDCRAFT/))은 현재 xlsx파일로 지원되고 있으나, json형태로 변환시켜주는 [xlsx2json.py](HANDCRAFT/Result/xlsx2json.py)를 사용하여 json형태로 변환할 수 있습니다.

사칙연산유형 데이터셋만 존재하는 MATHWPS/MATHQA 기반 데이터셋과 달리 HANDCRAFT 데이터셋들은 새로운 유형의 문제들이 포함되었습니다. 각 유형은 아래와 같습니다. 새로운 유형 데이터셋은 추후에도 계속 업데이트 될 예정입니다.

* 0_x : Validation set (아래 유형 모두 포함)
* 1_x : 사칙연산
* 2_x : 줄세우기
* 3_x : 소인수분해

