# Generated by Django 3.2.5 on 2021-09-24 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strName', models.CharField(max_length=50, verbose_name='施設名')),
                ('password', models.CharField(max_length=50, verbose_name='パスワード')),
                ('datePublish', models.DateField(auto_now_add=True, verbose_name='登録日時')),
            ],
            options={
                'verbose_name': '施設',
                'verbose_name_plural': '施設',
            },
        ),
        migrations.CreateModel(
            name='MemoMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strTaglist', models.CharField(max_length=50, verbose_name='タグリスト表示用')),
                ('numMemotype', models.IntegerField(default=1, verbose_name='メモタイプ')),
                ('strMainText', models.TextField(blank=True, verbose_name='本文')),
                ('listReceiver', models.CharField(blank=True, max_length=100, null=True, verbose_name='受信者リスト')),
                ('datePublish', models.DateTimeField(verbose_name='作成日時')),
                ('dateRegist', models.DateTimeField(verbose_name='登録日時')),
                ('keyFacility', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.facility', verbose_name='施設')),
                ('keyFollowId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follow', to='core.memomain', verbose_name='転送メモ')),
                ('keyParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='core.memomain', verbose_name='親メモ')),
                ('keyReplyBase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reply', to='core.memomain', verbose_name='スレッド')),
            ],
            options={
                'verbose_name': 'メモ',
                'verbose_name_plural': 'ノート',
            },
        ),
        migrations.CreateModel(
            name='OperateUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strName', models.CharField(max_length=50, verbose_name='ユーザー名')),
                ('password', models.CharField(max_length=50, verbose_name='パスワード')),
                ('datePublish', models.DateTimeField(verbose_name='登録日時')),
                ('numStatus', models.IntegerField(default=1, verbose_name='ステータス')),
                ('keyFacility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.facility', verbose_name='施設')),
            ],
            options={
                'verbose_name': '実施者',
                'verbose_name_plural': 'グループ',
            },
        ),
        migrations.CreateModel(
            name='TagMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strTagName', models.CharField(max_length=20, verbose_name='タグ名')),
                ('numTagType', models.IntegerField(verbose_name='タグタイプ')),
                ('numTagRank', models.IntegerField(verbose_name='タグランク')),
                ('datePublish', models.DateTimeField(verbose_name='登録日')),
                ('strSuffix', models.CharField(blank=True, max_length=50, verbose_name='数字タグの単位')),
                ('facilityId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.facility', verbose_name='所属施設')),
            ],
            options={
                'verbose_name': 'タグ',
                'verbose_name_plural': 'タグ',
            },
        ),
        migrations.CreateModel(
            name='UserTagConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numTagStatus', models.IntegerField(default=0, verbose_name='タグ設定')),
                ('boolIsShownInList', models.BooleanField(default=False, verbose_name='一覧表示')),
                ('keyOperateUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.operateuser', verbose_name='ユーザー')),
                ('keyTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tagmain', verbose_name='タグ')),
            ],
            options={
                'verbose_name': 'タグ利用設定',
                'verbose_name_plural': 'タグ利用設定',
            },
        ),
        migrations.CreateModel(
            name='TagSearchIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRegist', models.DateTimeField(null=True, verbose_name='登録日時')),
                ('keyFacility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.facility', verbose_name='施設')),
                ('keyMemoMain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.memomain', verbose_name='メモ')),
                ('keyTagMain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tagmain', verbose_name='タグ')),
            ],
            options={
                'verbose_name': 'タグ検索',
                'verbose_name_plural': 'タグ検索',
            },
        ),
        migrations.CreateModel(
            name='TagInFormatedMemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numTagPhase', models.IntegerField(default=-1, verbose_name='フェーズ')),
                ('strGroup', models.CharField(max_length=50, verbose_name='グループ')),
                ('strShow', models.CharField(blank=True, max_length=100, verbose_name='表示用数列')),
                ('strHide', models.CharField(blank=True, max_length=100, verbose_name='消滅用数列')),
                ('keyTagMain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tagmain', verbose_name='タグ')),
            ],
            options={
                'verbose_name': '誘導入力方タグ',
                'verbose_name_plural': '誘導入力方タグ',
            },
        ),
        migrations.AddField(
            model_name='operateuser',
            name='keyTagPlace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place', to='core.tagmain', verbose_name='所属タグ'),
        ),
        migrations.AddField(
            model_name='operateuser',
            name='tagId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='core.tagmain'),
        ),
        migrations.CreateModel(
            name='NoticeMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numNoticeType', models.IntegerField(default=-1, verbose_name='通知タイプ')),
                ('boolHasRead', models.BooleanField(default=False, verbose_name='既読')),
                ('keyMemoMain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.memomain')),
                ('keyOperateUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.operateuser')),
            ],
        ),
        migrations.AddField(
            model_name='memomain',
            name='keySender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.operateuser', verbose_name='送信者'),
        ),
        migrations.CreateModel(
            name='IsUserReadInMemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasFavorite', models.BooleanField(default=True)),
                ('keyMemoMain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.memomain')),
                ('keyOperateUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.operateuser')),
            ],
            options={
                'verbose_name': '既読',
                'verbose_name_plural': '既読',
            },
        ),
        migrations.CreateModel(
            name='IsUserFavoriteInMemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasFavorite', models.BooleanField(default=True)),
                ('keyMemoMain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.memomain')),
                ('keyOperateUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.operateuser')),
            ],
            options={
                'verbose_name': 'お気に入り',
                'verbose_name_plural': 'お気に入り',
            },
        ),
        migrations.CreateModel(
            name='GuestMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strGuestName', models.CharField(max_length=30, verbose_name='利用者名')),
                ('numStatus', models.IntegerField(default=1, verbose_name='状態')),
                ('keyPlaceTagMain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guest_place', to='core.tagmain', verbose_name='場所タグ')),
                ('keyTagMain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_main', to='core.tagmain', verbose_name='所属タグ')),
            ],
            options={
                'verbose_name': '利用者メイン',
                'verbose_name_plural': '利用者メイン',
            },
        ),
    ]
