class CustomAuthToken(ObtainAuthToken):

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data,context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		try:
			token = Token.objects.get(user=user).delete()
		except:
			pass
		token, created = Token.objects.get_or_create(user=user)
		try:
			fran_user = UserExtraData.objects.get(which_user=user)
			if fran_user.user_type == 's' or fran_user.user_type == 'f':
				return Response({
				'token': token.key,
				'user_id': user.pk,
				'username':user.username,
				'user_type': fran_user.user_type,
				})
		except:
			pass
		try:
			super_user = user.is_superuser
		except:
			return Response({'Error':'Unauthorized user!!'}, status=status.HTTP_401_UNAUTHORIZED)
		return Response({
		'token': token.key,
		'user_id': user.pk,
		'username':user.username,
		'super_user': super_user,
		})
		