from django.shortcuts import render, redirect
from django.http import Http404
from .models import Post

# Create your views here.
post_db = [
    {
        'id': 1,
        'title': '블로그 포스트 1',
        'content': """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eu libero molestie, cursus lacus vitae, iaculis metus. Morbi libero ligula, fermentum non enim eu, euismod pulvinar urna. Mauris at justo eget dui suscipit condimentum ac a mi. Nunc a imperdiet sem, tincidunt laoreet turpis. In tristique pulvinar sapien, non ultricies tortor scelerisque in. Aliquam ut ante eget justo maximus feugiat. Morbi sed viverra lorem. Aenean luctus tortor vitae urna sodales, ac ornare nisi semper. Maecenas suscipit justo urna, at vestibulum risus egestas eu.

Pellentesque id neque at justo efficitur auctor id quis arcu. Praesent mauris mi, laoreet at lacus quis, dictum volutpat nulla. Integer ullamcorper dictum arcu, sed vulputate diam eleifend vel. Integer posuere lacus eget massa dictum, ac ullamcorper magna sagittis. Sed turpis erat, rutrum vulputate tempor euismod, bibendum vitae odio. Praesent nec risus nec eros auctor molestie. Praesent congue eget libero at imperdiet. Mauris a euismod neque. Maecenas convallis dolor diam, at molestie magna imperdiet vel. Integer et venenatis augue.

Curabitur non leo vel dolor feugiat eleifend vitae ut mi. Morbi quis finibus purus. Aliquam ac ligula metus. Maecenas tellus elit, interdum a purus a, maximus sollicitudin sapien. In at fermentum sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In volutpat lectus id mi sagittis gravida. In fringilla eros ut est malesuada posuere.

Aliquam sodales risus lacus, finibus laoreet arcu facilisis id. Integer vitae tellus a ex malesuada pretium. Donec ac dapibus nunc. Aliquam ullamcorper orci ac ex ullamcorper posuere. Cras pretium dolor blandit ante ultricies, in rutrum massa laoreet. Praesent lacus lacus, tempor vestibulum blandit hendrerit, aliquam et massa. Ut eget iaculis ex. Praesent a risus ac mauris molestie tristique sit amet id sapien. Fusce in nisl leo. Donec accumsan, eros vitae malesuada porta, diam felis placerat velit, vitae consequat purus tortor et felis. Mauris nibh ipsum, egestas nec consequat vitae, gravida at lectus. Donec finibus sagittis tortor, ut porttitor lectus finibus in. Maecenas nunc felis, tempus in suscipit vel, accumsan ac neque.

Integer auctor est et aliquet gravida. Donec tincidunt urna vel mollis ornare. Curabitur blandit sit amet leo pulvinar bibendum. Donec quis justo ac odio venenatis ornare. Nulla lobortis maximus enim, vel eleifend nisi. Curabitur tincidunt purus lectus, in euismod libero ullamcorper ut. Aliquam id mollis lacus. Etiam tellus nibh, tempus at vestibulum sit amet, blandit nec justo. Maecenas sed fringilla lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eleifend ullamcorper ligula, quis pharetra magna efficitur et. Duis maximus nulla lectus, non mollis augue sagittis a. Aliquam orci urna, pharetra et tincidunt ut, ornare ut magna. Proin semper quam orci, eu semper quam dictum eu. Donec semper, felis quis feugiat malesuada, quam dui commodo nisl, a sagittis lectus sem nec est. Vestibulum ac ligula ornare, eleifend ligula non, tincidunt ligula.
""",
        'date_posted': '2024-01-02 12:34:56'
    },
    {
        'id': 2,
        'title': 'Blog Post 2',
        'content': """외국인은 국제법과 조약이 정하는 바에 의하여 그 지위가 보장된다. 대통령은 법률안의 일부에 대하여 또는 법률안을 수정하여 재의를 요구할 수 없다. 국가는 농수산물의 수급균형과 유통구조의 개선에 노력하여 가격안정을 도모함으로써 농·어민의 이익을 보호한다. 체포·구속·압수 또는 수색을 할 때에는 적법한 절차에 따라 검사의 신청에 의하여 법관이 발부한 영장을 제시하여야 한다. 다만, 현행범인인 경우와 장기 3년 이상의 형에 해당하는 죄를 범하고 도피 또는 증거인멸의 염려가 있을 때에는 사후에 영장을 청구할 수 있다.

국무총리는 대통령을 보좌하며, 행정에 관하여 대통령의 명을 받아 행정각부를 통할한다. 선거운동은 각급 선거관리위원회의 관리하에 법률이 정하는 범위안에서 하되, 균등한 기회가 보장되어야 한다. 국민의 자유와 권리는 헌법에 열거되지 아니한 이유로 경시되지 아니한다. 국토와 자원은 국가의 보호를 받으며, 국가는 그 균형있는 개발과 이용을 위하여 필요한 계획을 수립한다.

모든 국민은 헌법과 법률이 정한 법관에 의하여 법률에 의한 재판을 받을 권리를 가진다. 헌법재판소 재판관은 탄핵 또는 금고 이상의 형의 선고에 의하지 아니하고는 파면되지 아니한다. 누구든지 체포 또는 구속을 당한 때에는 적부의 심사를 법원에 청구할 권리를 가진다. 모든 국민은 주거의 자유를 침해받지 아니한다. 주거에 대한 압수나 수색을 할 때에는 검사의 신청에 의하여 법관이 발부한 영장을 제시하여야 한다.

누구든지 체포 또는 구속을 당한 때에는 즉시 변호인의 조력을 받을 권리를 가진다. 다만, 형사피고인이 스스로 변호인을 구할 수 없을 때에는 법률이 정하는 바에 의하여 국가가 변호인을 붙인다. 위원은 정당에 가입하거나 정치에 관여할 수 없다. 사면·감형 및 복권에 관한 사항은 법률로 정한다. 국회의원의 수는 법률로 정하되, 200인 이상으로 한다.

법률은 특별한 규정이 없는 한 공포한 날로부터 20일을 경과함으로써 효력을 발생한다. 국무총리는 국무위원의 해임을 대통령에게 건의할 수 있다. 국회의원과 정부는 법률안을 제출할 수 있다. 근로자는 근로조건의 향상을 위하여 자주적인 단결권·단체교섭권 및 단체행동권을 가진다. 대법원은 법률에 저촉되지 아니하는 범위안에서 소송에 관한 절차, 법원의 내부규율과 사무처리에 관한 규칙을 제정할 수 있다.

국정감사 및 조사에 관한 절차 기타 필요한 사항은 법률로 정한다. 예비비는 총액으로 국회의 의결을 얻어야 한다. 예비비의 지출은 차기국회의 승인을 얻어야 한다. 정부는 회계연도마다 예산안을 편성하여 회계연도 개시 90일전까지 국회에 제출하고, 국회는 회계연도 개시 30일전까지 이를 의결하여야 한다.

모든 국민은 법률이 정하는 바에 의하여 납세의 의무를 진다. 대한민국의 영토는 한반도와 그 부속도서로 한다. 대통령은 제3항과 제4항의 사유를 지체없이 공포하여야 한다. 대통령은 조약을 체결·비준하고, 외교사절을 신임·접수 또는 파견하며, 선전포고와 강화를 한다. 일반사면을 명하려면 국회의 동의를 얻어야 한다.

""",
        'date_posted': '2024-01-05 12:34:56'
    }
]

def posts(request):
    if request.method == 'POST':
        post = Post.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content')
        )
        return redirect('read_post', post.id)
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts.html', context)

def new_post(request):
    return render(request, 'new_post.html')

def edit_post(request, id: int):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('read_post', post.id)
    return render(request, 'edit_post.html', {'post': post})

def read_post(request, id: int):
    try :
        post = Post.objects.get(id=id)
        return render(request, 'read_post.html', {'post': post})
    except Post.DoesNotExist:
        raise Http404('Post not found')

def delete_post(request, id: int):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('posts')