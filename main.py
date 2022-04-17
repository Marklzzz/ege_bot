from sdamgia import SdamGIA
from pprint import pprint

sdamgia = SdamGIA()

subject = 'math'
id = '1001'
pprint(sdamgia.get_problem_by_id(subject, id)[])

subject = 'math'
problems = {'full': 1}
res = sdamgia.generate_test(subject, problems)
print(sdamgia.generate_pdf('math', res, pdf='h'))